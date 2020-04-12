<template>
	<ul class="list-unstyled">
		<command-sidebar-entry v-for="(subgroup, subgroupId) in subgroups" :subgroup="subgroup" :subgroupId="subgroupId"
							   :key="subgroupId"></command-sidebar-entry>
	</ul>
</template>

<script>
	import CommandSidebarEntry from "./CommandSidebarEntry";

	export default {
		components: {
			CommandSidebarEntry
		},
		props: {
			subgroups: {
				type: Object,
				required: true
			}
		}
	}
</script>