<template>
	<div>
		<command-group v-for="(commandGroup, commandGroupId) in subgroups" :depth="depth"
					   :command-group-id="commandGroupId" :command-group="commandGroup"
					   :key="commandGroupId"/>
	</div>
</template>

<script>
	import CommandGroup from "./CommandGroup";

	export default {
		components: {
			CommandGroup
		},
		props: {
			subgroups: {
				type: Object,
				required: true
			},
			depth: {
				type: Number,
				required: true
			}
		}
	}
</script>