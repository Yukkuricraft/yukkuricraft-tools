<template>
	<li>
		<template v-if="subgroup.isGroup">
			<a data-toggle="collapse" aria-expanded="false" class="dropdown-toggle"
			   :href="'#commandsSidebar-' + subgroupId">{{ subgroup.menuName }}</a>
			<command-sidebar-entries :id="'commandsSidebar-' + subgroupId" class="collapse"
									 :subgroups="subgroup.subgroups"></command-sidebar-entries>
		</template>
		<template v-else>
			<a :href="'#commands-' + subgroupId">{{ subgroup.menuName }}</a>
		</template>
	</li>
</template>

<script>

	export default {
		components: {
			CommandSidebarEntries: () => import("./CommandSidebarEntries")
		},
		props: {
			subgroup: {
				type: Object,
				required: true
			},
			subgroupId: {
				type: String,
				required: true
			}
		}
	}
</script>