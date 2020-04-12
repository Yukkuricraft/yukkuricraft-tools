const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyPlugin = require('copy-webpack-plugin');
module.exports = {
	entry: {
		'styling': './src/styling.js',
		'info': './src/app.js',
		'rank_staff': './src/rank_staff/rank_staff.js',
		'commands': './src/commands/commands.js'
	},
	output: {
		filename: '[name].js',
		path: path.resolve(__dirname, 'dist')
	},
	plugins: [new MiniCssExtractPlugin(), new CopyPlugin([{from: 'src/commands/images', to: 'assets/images'}])],
	module: {
		rules: [
			{
				test: /\.(scss)$/,
				use: [
					MiniCssExtractPlugin.loader,
					'css-loader',
					'postcss-loader',
					{
						loader: 'sass-loader',
						options: {
							sassOptions: {
								functions: require('chromatic-sass')
							}
						}
					}
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
