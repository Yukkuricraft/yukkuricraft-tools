const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
	entry: {
		'styling': './src/styling.js',
		'info': './src/info/app.js',
		'download': './src/download/download.js'
	},
	output: {
		filename: '[name].js',
		path: path.resolve(__dirname, 'dist')
	},
	plugins: [new MiniCssExtractPlugin(), new CopyPlugin([{from: 'src/images', to: 'assets/images'}])],
	module: {
		rules: [
			{
				test: /\.(scss)$/,
				use: [
					MiniCssExtractPlugin.loader,
					'css-loader',
					'postcss-loader',
					'sass-loader'
				]
			},
			{
				test: /\.html$/i,
				use: ['file-loader?name=[name].[ext]', 'extract-loader', 'html-loader'],
			},
			{
				test: /\.(png|svg|jpg|gif)$/,
				use: {
					loader: 'file-loader',
					options: {
						esModule: false, //https://github.com/peerigon/extract-loader/issues/67
						outputPath: 'assets/images'
					}
				}
			}
		]
	},
	optimization: {
		splitChunks: {
			cacheGroups: {
				vendors: {
					name: "js-vendors",
					chunks: "initial",
					test: /[\\/]node_modules[\\/]/,
					priority: 10,
					enforce: true
				},
				commons: {
					name: "commons",
					chunks: "initial",
					minChunks: 2,
				},
			}
		}
	}
};
