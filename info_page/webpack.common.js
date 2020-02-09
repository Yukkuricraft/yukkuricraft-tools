const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
	entry: './src/app.js',
	output: {
		filename: '[name].js',
		path: path.resolve(__dirname, 'dist')
	},
	plugins: [new MiniCssExtractPlugin()],
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
