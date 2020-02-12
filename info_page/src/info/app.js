import './index.html';

import {createStaffList} from './staffRenderer'
import {createCommandsList} from "./commandRenderer";

document.addEventListener('DOMContentLoaded', onReady, false);

function onReady() {
	createStaffList();
	createCommandsList();
}
