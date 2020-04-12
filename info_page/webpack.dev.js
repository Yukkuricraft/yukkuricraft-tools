const merge = require('webpack-merge');
const common = require('./webpack.common.js');

const CopyPlugin = require('copy-webpack-plugin');

module.exports = merge(common, {
	mode: 'development',
	devtool: 'inline-source-map',
	plugins: [
		new CopyPlugin([{from: 'src/pages/commands/images', to: 'assets/images/commands'}])
	]
});
