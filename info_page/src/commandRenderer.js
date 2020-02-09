import $ from "jquery";
import cmds from "./commands";

function makeCommandNode(command) {
	let aliases = Array.isArray(command.aliases) ? command.aliases : [command.aliases];
	let aliasesStr = aliases.join(' | ');

	let args = typeof command.arguments !== 'undefined' ? ' ' + command.arguments : '';
	let commandStr = '/' + aliasesStr + args;

	return [
		$(`<span class="command">`).append($('<strong>').text(commandStr)),
		' - ' + command.description
	]
}

function createCommandList(id, commands) {
	return [
		$('<h3 class="scrolltarget">').text(commands.displayName).attr('id', 'commands-' + id),
		$('<ul>').append(commands.commands.map(makeCommandNode).map(node => $('<li>').append(node)))
	]
}

export function createCommandsList() {
	let commandsSection = $('#commandsSection');
	let navbarCommandsDropdown = $('#navbar-commands-dropdown');

	for (let id in cmds) {
		if (cmds.hasOwnProperty(id)) {
			commandsSection.append(createCommandList(id, cmds[id]));
			navbarCommandsDropdown.append($('<a class="dropdown-item">')
				.attr('href', '#commands-' + id)
				.text(cmds[id].displayName));
		}
	}
}