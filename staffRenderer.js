import $ from "jquery";
import {staff} from "./staff";

async function mcUsername(uuid, fallback) {
	try {
		let res = await fetch('https://api.minetools.eu/profile/' + uuid.replace('-', ''))

		if (res.status !== 200) {
			return fallback;
		} else {
			let profile = await res.json();
			return profile.decodec.profileName
		}
	} catch (e) {
		return fallback
	}
}

async function createAccountsNode(accounts) {
	async function createSingleNode(account) {
		return [
			$(`<img src="https://mc-heads.net/avatar/${account.uuid}/32">`),
			document.createTextNode(' ' + await mcUsername(account.uuid, account.name))
		]
	}

	if (accounts.length > 1) {
		let accountNodes = await Promise.all(accounts.map(createSingleNode));
		return $('<ul class="list-unstyled">').append(accountNodes.map(nodes => $('<li>').append(nodes)))
	} else if (accounts) {
		return $('<div>').append(await createSingleNode(accounts[0]))
	} else {
		return $("None")
	}
}

async function createMemberNode(hasDescription, member) {
	let accountsArr = Array.isArray(member.mcAccounts) ? member.mcAccounts : [member.mcAccounts];
	let accounts = await createAccountsNode(accountsArr);

	let row = $('<tr>');

	if (hasDescription) {
		let desc = member.description ? member.description : '';
		return row.append($(`<td>${member.name}</td>`), $('<td>').append(accounts), $('<td>').append(desc));
	} else {
		return row.append($(`<td>${member.name}</td>`), $('<td>').append(accounts));
	}
}

async function makeStaffNode(obj) {
	let elem = $('<table>');
	elem.id = 'staff-' + obj.id;
	elem.addClass('table');

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

	let memberNodes = await Promise.all(obj.members.map(member => createMemberNode(obj.hasDescription, member)));

	elem.append(memberNodes);

	return elem
}

export function createStaffList() {
	let staffData = $('#staffData');
	staffData.innerHTML = '';
	Promise.all(staff.map(makeStaffNode)).then(staffNodes => {
		staffData.append(staffNodes)
	});
}