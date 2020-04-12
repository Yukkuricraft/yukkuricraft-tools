import Vue from "vue";

export default Vue.component('heading', {
	render(createElement, context) {
		return createElement(
			'h' + this.level,
			this.$slots.default
		)
	},
	props: {
		level: {
			type: Number,
			required: true
		}
	}
})