const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
	entry: {
		'app': [
			'./src/styling.js',
			'./src/app.js'
		]
	},
	output: {
		filename: '[name].js',
		path: path.resolve(__dirname, 'dist'),
		publicPath: '/'
	},
	plugins: [
		new VueLoaderPlugin(),
		new HtmlWebpackPlugin({
			title: 'Yukkuricraft Info',
			filename: 'index.html',
			template: 'src/index.html'
		})
	],
	module: {
		rules: [
			{
				test: /\.(scss)$/,
				use: [
					process.env.NODE_ENV !== 'production' ? 'vue-style-loader' : MiniCssExtractPlugin.loader,
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
				test: /\.(png|svg|jpg|gif)$/,
				use: {
					loader: 'file-loader',
					options: {
						esModule: false, //https://github.com/peerigon/extract-loader/issues/67
						outputPath: 'assets/images'
					}
				}
			},
			{
				test: /\.vue$/,
				loader: 'vue-loader'
			},
			{
				resourceQuery: /blockType=i18n/,
				type: 'javascript/auto',
				loader: '@intlify/vue-i18n-loader'
			}
		]
	},
	resolve: {
		alias: {
			'vue$': 'vue/dist/vue.esm.js'
		},
		extensions: ['*', '.js', '.vue', '.json']
	},
	devServer: {
		historyApiFallback: true
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
