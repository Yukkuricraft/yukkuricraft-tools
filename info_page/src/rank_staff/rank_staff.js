import './rank_staff.html';

import {createStaffList} from './staffRenderer'

document.addEventListener('DOMContentLoaded', onReady, false);

function onReady() {
	createStaffList();
}
