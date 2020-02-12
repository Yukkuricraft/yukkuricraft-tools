import $ from "jquery";
import cmds from "./commands";
import markdownIt from "markdown-it"

const md = markdownIt({linkify: true, typographer: true});

function makeCommandNode(command, query) {
	function matchesQuery(str) {
		if (!query) {
			return true;
		} else {
			return str.toLowerCase().includes(query.toLowerCase());
		}
	}

	let aliases = Array.isArray(command.aliases) ? command.aliases : [command.aliases];

	if (aliases.some(matchesQuery) || command.tags.some(matchesQuery) || matchesQuery(command.description)) {
		let aliasesStr = aliases.join(' | ');

		let args = typeof command.arguments !== 'undefined' ? ' ' + command.arguments : '';
		let commandStr = '/' + aliasesStr + args;
		let mdContent = $(md.render(command.description));
		mdContent.find('img').attr('width', '100%');

		return [
			$(`<span class="command">`).append($('<strong>').text(commandStr)),
			mdContent
		]
	} else {
		return []
	}
}

function createCommandList(level, id, commands, query) {
	let header = $(`<h${3 + level} class="scrolltarget">`).text(commands.displayName).attr('id', 'commands-' + id);
	let desc = typeof commands.description !== 'undefined' ? md.render(commands.description) : null;

	if (typeof commands.isGroup !== 'undefined' && commands.isGroup) {
		let thisParent = $('<div>');
		let [commandChildren, dropdownChildren] = createSubgroups(level + 1, commands.subgroups, query);

		if (commandChildren.length) {
			return [
				[
					header, desc, thisParent.append(commandChildren)
				].filter(Boolean),
				dropdownChildren
			]
		} else {
			return [[], []]
		}
	} else {
		let commandNodes = commands.commands.map(c => makeCommandNode(c, query)).filter(arr => arr.length);

		if (commandNodes.length) {
			return [
				[
					header,
					desc,
					$('<ul>').append(commandNodes.map(node => $('<li>').append(node)))
				].filter(Boolean),
				[]
			]
		} else {
			return [[], []]
		}
	}
}

function createSubgroups(level, subgroup, query) {
	let dropdownItems = [];
	let commandItems = [];

	for (let id in subgroup) {
		if (subgroup.hasOwnProperty(id)) {
			let [commandList, innerDropdownItems] = createCommandList(level, id, subgroup[id], query);

			if (commandList.length) {
				commandItems.push(...commandList);
				dropdownItems.push($('<a class="dropdown-item">')
					.attr('href', '#commands-' + id)
					.text(subgroup[id].menuName));
				dropdownItems.push(...innerDropdownItems);
			}
		}
	}

	return [commandItems, dropdownItems]
}

function renderCommandList(query) {
	let navbarCommandsDropdown = $('#navbar-commands-dropdown');
	let commandGroups = $('#commandGroups');
	navbarCommandsDropdown.empty();
	commandGroups.empty();

	let [commandNodes, dropdownNodes] = createSubgroups(0, cmds, query);

	commandGroups.append(commandNodes);
	navbarCommandsDropdown.append(dropdownNodes);
}

export function createCommandsList() {
	renderCommandList('');

	$('#commandsSearch').on('input', e => renderCommandList(e.target.value))
}