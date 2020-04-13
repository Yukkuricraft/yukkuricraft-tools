const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const path = require('path');

const CopyPlugin = require('copy-webpack-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const PrerenderSPAPlugin = require('prerender-spa-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const Renderer = PrerenderSPAPlugin.PuppeteerRenderer

let isCI = typeof process.env.CI !== 'undefined' && process.env.CI

module.exports = merge(common, {
	mode: 'production',
	devtool: 'source-map',
	plugins: [
		new PrerenderSPAPlugin({
			staticDir: path.join(__dirname, 'dist'),
			indexPath: path.join(__dirname, 'dist', 'index.html'),
			routes: [
				'/',
				'/rules',
				'/ranks_staff',
				'/commands',
				'/downloads/gensokyo',
				'/downloads/survival'
			],
			renderer: new Renderer({
				headless: true,
				renderAfterDocumentEvent: 'render-event',
				executablePath: isCI ? 'google-chrome-unstable' : undefined
			}),
		}),
		new MiniCssExtractPlugin(),
		new CopyPlugin([{from: 'src/pages/commands/images', to: 'assets/images/commands'}])
	],
	optimization: {
		minimizer: [
			new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})
		]
	}
});
