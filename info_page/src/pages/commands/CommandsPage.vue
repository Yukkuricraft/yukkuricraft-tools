<template>
	<sidebar-page parallax-class="parallax-commands">
		<template v-slot:sidebar>
			<div class="sidebar-header">
				<h2>Commands</h2>
			</div>

			<command-sidebar-entries class="sidebar-components" :subgroups="commands"></command-sidebar-entries>
		</template>

		<template v-slot:parallax>
			<h1>Commands</h1>
			<p>Find commonly used commands here</p>
		</template>


		<h2 id="commands" class="scrolltarget">Command List</h2>
		<div id="commandsSection">
			<p style="font-size:18px;color:#aaafad">
				Arguments in "[" and "]" are optional. Arguments in "&lt;" and "&gt;" are required for the
				command
				to
				work!
			</p>
			<p style="font-size:12px;color:#aaafad">
				This is nowhere near a complete list of commands, just some of the basics!
			</p>

			<div class="form-group">
				<label for="commandsSearch">Search:</label>
				<input id="commandsSearch" type="text" class="form-control" placeholder="Search commands..."
					   v-model="filter">
			</div>

			<div id="commandGroups">
				<command-groups :subgroups="commands" :depth="0"/>
			</div>
		</div>
	</sidebar-page>
</template>

<script>
	import InfoFooter from "../../components/InfoFooter";
	import ParallaxImage from "../../components/ParallaxImage";
	import CommandGroups from "./CommandGroups";
	import CommandSidebarEntries from "./CommandSidebarEntries";
	import SidebarPage from "../../layout/SidebarPage";

	import generalCmds from "./general_commands";
	import tpCmds from "./tp_commands";
	import chatCmds from "./chat_commands";
	import lwcCmds from "./lwc_commands";
	import hshCmds from "./hsh_commands";

	let allCommands = {...generalCmds, ...tpCmds, ...chatCmds, ...lwcCmds, ...hshCmds}

	export default {
		components: {
			SidebarPage,
			CommandSidebarEntries,
			InfoFooter,
			ParallaxImage,
			CommandGroups,
		},
		data() {
			return {
				filter: "",
				sidebarActive: false
			}
		},
		computed: {
			commands() {
				let filter = this.filter;

				function matchesQuery(str) {
					return str.toLowerCase().includes(filter.toLowerCase())
				}

				function commandAliases(command) {
					return Array.isArray(command.aliases) ? command.aliases : [command.aliases];
				}

				function commandMatchesQuery(command) {
					return commandAliases(command).some(matchesQuery) ||
						command.tags.some(matchesQuery) ||
						matchesQuery(command.description)
				}

				function filterSubgroup(subgroup) {
					if (typeof subgroup.isGroup !== 'undefined' && subgroup.isGroup) {
						let subsubgroups = filterSubgroups(subgroup.subgroups);

						if (Object.entries(subsubgroups).length) {
							subgroup.subgroups = subsubgroups
							return subgroup
						} else {
							return null
						}
					} else {
						console.log(subgroup.commands)
						let validCommands = subgroup.commands.filter(commandMatchesQuery);
						console.log(validCommands)

						if (validCommands.length) {
							subgroup.commands = validCommands
							return subgroup
						} else {
							console.log('Filtering out subgroup')
							return null
						}
					}

				}

				function filterSubgroups(subgroups) {
					Object.entries(subgroups).forEach(([id, subgroup]) => {
						let newSubgroup = filterSubgroup(subgroup)
						if (newSubgroup === null) {
							delete subgroups[id]
						} else {
							subgroups[id] = newSubgroup
						}
					});

					return subgroups
				}

				let commandsCopy = JSON.parse(JSON.stringify(allCommands))

				console.log('Starting filtering')
				return this.filter.length ? filterSubgroups(commandsCopy) : commandsCopy
			}
		}
	}
</script>
