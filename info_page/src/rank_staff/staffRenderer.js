import $ from "jquery";
import {staff} from "./staff";

async function mcUsername(uuid, fallback) {
	let errorMsg = `Failed to get name for uuid ${uuid}, using fallback ${fallback} instead`;

	try {
		let res = await fetch('https://api.minetools.eu/profile/' + uuid.replaceAll('-', ''));

		if (res.status !== 200) {
			console.warn(errorMsg);
			return fallback;
		} else {
			let profile = await res.json();

			if(typeof profile.error !== 'undefined') {
				console.warn(errorMsg + '. Error: ' + profile.error);
				return fallback;
			}
			else {
				return profile.decoded.profileName
			}
		}
	} catch (e) {
		console.warn(errorMsg + '. Error: ' + e);
		return fallback
	}
}

function createAccountsNode(accounts) {
	function createSingleNode(account) {
		let imgNode = $(`<img src="https://mc-heads.net/avatar/${account.uuid}/32">`);
		let textNode = document.createTextNode(' ' + account.name);

		let setRealUsername = function () {
			mcUsername(account.uuid, account.name).then(name => {
				textNode.data = ' ' + name;
			})
		};

		return [
			[
				imgNode,
				textNode
			],
			setRealUsername
		]
	}

	if (accounts.length > 1) {
		let [accountNodes, callbacks] = unzip(accounts.map(createSingleNode));
		return [$('<ul class="list-unstyled">').append(accountNodes.map(nodes => $('<li>').append(nodes))), callbacks]
	} else if (accounts) {
		let [node, callback] = createSingleNode(accounts[0]);
		return [$('<div>').append(node), callback]
	} else {
		return $("None")
	}
}

function createMemberNode(hasDescription, member) {
	let accountsArr = Array.isArray(member.mcAccounts) ? member.mcAccounts : [member.mcAccounts];
	let [accounts, callbacks] = createAccountsNode(accountsArr);

	let row = $('<tr>').append($(`<td>${member.name}</td>`), $('<td>').append(accounts));

	if (hasDescription) {
		let desc = member.description ? member.description : '';
		row.append($('<td>').append(desc));
		return [row, callbacks];
	} else {
		return [row, callbacks];
	}
}

function makeStaffNode(obj) {
	let elem = $('<table class="table smaller-sm-text">');
	elem.id = 'staff-' + obj.id;

	let colgroup = $('<colgroup>');

	function col(percent) {
		return $(`<col style="width: ${percent}%;">`)
	}

	if (obj.hasDescription) {
		colgroup.append(col(20), col(30), col(50));
	} else {
		colgroup.append(col(20), col(80));
	}

	elem.append(colgroup);

	let nameCell = $(`<th colspan="1">${obj.displayName}</th>`);
	let accountNameCell = $(`<th colspan="${obj.hasDescription ? '2' : '1'}">MC Accounts</th>`);
	elem.append($('<thead>').append($('<tr>').append(nameCell, accountNameCell)));

	let [memberNodes, callbacks] = unzip(obj.members.map(member => createMemberNode(obj.hasDescription, member)));

	elem.append(memberNodes);

	return [elem, callbacks.flat()]
}

function unzip(xs) {
	let res = [[], []];

	for (let i = 0; i < xs.length; i++) {
		res[0].push(xs[i][0]);
		res[1].push(xs[i][1]);
	}

	return res
}

export function createStaffList() {
	let staffData = $('#staffData');
	staffData.innerHTML = '';
	let [nodes, callbacks] = unzip(staff.map(makeStaffNode));

	staffData.append(nodes);

	for (let fn of callbacks.flat()) {
		fn();
	}
}