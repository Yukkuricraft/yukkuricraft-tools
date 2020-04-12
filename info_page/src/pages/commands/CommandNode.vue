<template>
	<div>
		<span class="command"><strong>{{ commandStr }}</strong></span>
		<div v-html="description"></div>
	</div>
</template>

<script>
	import markdownIt from "markdown-it"

	const md = markdownIt({linkify: true, typographer: true});

	export default {
		props: {
			command: {
				type: Object,
				required: true
			}
		},
		computed: {
			commandStr() {
				let aliasesStr = Array.isArray(this.command.aliases) ? this.command.aliases.join(' | ') : this.command.aliases;
				let args = typeof this.command.arguments !== 'undefined' ? ' ' + this.command.arguments : '';
				return '/' + aliasesStr + args
			},
			description() {
				return md.render(this.command.description)
			}
		}
	}
</script>