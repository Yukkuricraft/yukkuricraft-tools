const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
	entry: './src/app.js',
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
		]
	}
};
