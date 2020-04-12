import "./commands.html"

import {createCommandsList} from "./commandRenderer";
import generalCmds from "./general_commands.json"
import tpCmds from "./tp_commands.json"
import chatCmds from "./chat_commands.json"
import lwcCmds from "./lwc_commands.json"
import hshCmds from "./hsh_commands.json"

document.addEventListener('DOMContentLoaded', onReady, false);

function onReady() {
	let allCommands = {...generalCmds, ...tpCmds, ...chatCmds, ...lwcCmds, ...hshCmds}

	createCommandsList(allCommands);

	$('[data-spy="scroll"]').each(function () {
		$(this).scrollspy('refresh')
	})
}