import $ from "jquery";
import cmds from "./commands";

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

		return [
			$(`<span class="command">`).append($('<strong>').text(commandStr)),
			' - ' + command.description
		]
	} else {
		return []
	}
}

function createCommandList(id, commands, query) {
	let commandNodes = commands.commands.map(c => makeCommandNode(c, query)).filter(arr => arr.length);

	if (commandNodes.length) {
		return [
			$('<h3 class="scrolltarget">').text(commands.displayName).attr('id', 'commands-' + id),
			$('<ul>').append(commandNodes.map(node => $('<li>').append(node)))
		]
	} else {
		return []
	}
}

function renderCommandList(query) {
	let navbarCommandsDropdown = $('#navbar-commands-dropdown');
	let commandGroups = $('#commandGroups');
	navbarCommandsDropdown.empty();
	commandGroups.empty();

	for (let id in cmds) {
		if (cmds.hasOwnProperty(id)) {
			let commandList = createCommandList(id, cmds[id], query);

			if (commandList.length) {
				commandGroups.append(commandList);
				navbarCommandsDropdown.append($('<a class="dropdown-item">')
					.attr('href', '#commands-' + id)
					.text(cmds[id].displayName));
			}
		}
	}
}

export function createCommandsList() {
	renderCommandList('');

	$('#commandsSearch').on('input', e => renderCommandList(e.target.value))
}