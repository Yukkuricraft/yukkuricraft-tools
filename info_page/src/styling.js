import 'bootstrap';
import './scss/app.scss';
import $ from 'jquery';
import '@fortawesome/fontawesome-free/js/all'

$(document).ready(function () {

	$('.sidebar-toggler').on('click', function () {
		$($(this).data('target')).toggleClass('active');
	});
});