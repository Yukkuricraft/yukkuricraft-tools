<template>
	<div>
		<heading :id="'commands-' + commandGroupId" :level="3 + depth" class="scrolltarget">{{ commandGroup.displayName }}</heading>
		<div v-html="description"></div>
		<command-groups v-if="commandGroup.isGroup" :depth="depth + 1"
						:subgroups="commandGroup.subgroups"></command-groups>
		<ul v-else>
			<li v-for="command in commandGroup.commands">
				<command-node :command="command"></command-node>
			</li>
		</ul>
	</div>
</template>

<script>
	import Heading from "../../components/Heading";
	import CommandNode from "./CommandNode";

	import markdownIt from "markdown-it"

	const md = markdownIt({linkify: true, typographer: true});

	export default {
		components: {
			CommandGroups: () => import("./CommandGroups.vue"),
			CommandNode,
			Heading
		},
		props: {
			commandGroupId: {
				type: String,
				required: true
			},
			commandGroup: {
				type: Object,
				required: true
			},
			depth: {
				type: Number,
				required: true
			}
		},
		computed: {
			description() {
				return typeof this.commandGroup.description !== 'undefined' ? md.render(this.commandGroup.description) : null;
			}
		}
	}
</script>