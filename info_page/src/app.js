import 'bootstrap';
import './scss/app.scss';
import './index.html';

import $ from 'jquery'

import {createStaffList} from './staffRenderer'

document.addEventListener('DOMContentLoaded', onReady, false);

function onReady() {
	createStaffList();
}
