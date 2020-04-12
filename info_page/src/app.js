import Vue from 'vue'
import VueRouter from "vue-router";
import VueI18n from "vue-i18n";

import InfoPage from './pages/InfoPage'
import RulesPage from './pages/RulesPage'
import RanksStaffPage from './pages/RanksStaffPage'
import CommandsPage from './pages/commands/CommandsPage'
import DownloadGenso from "./pages/downloads/Download";
import DownloadSurvival from "./pages/downloads/DownloadSurvival";

import App from './App.vue'

Vue.use(VueRouter);
Vue.use(VueI18n);

const router = new VueRouter({
	base: '/',
	mode: 'history',
	routes: [
		{
			path: '/',
			name: 'info',
			component: InfoPage
		},
		{
			path: '/rules',
			name: 'rules',
			component: RulesPage
		},
		{
			path: '/ranks_staff',
			name: 'ranks_staff',
			component: RanksStaffPage
		},
		{
			path: '/commands',
			name: 'commands',
			component: CommandsPage
		},
		{
			path: '/downloads/gensokyo',
			name: 'download_genso',
			component: DownloadGenso
		},
		{
			path: '/downloads/survival',
			name: 'download_survival',
			component: DownloadSurvival
		}
	]
})

const app = new Vue({
	el: '#app',
	render: createElement => createElement(App),
	router,
	mounted() {
		// You'll need this for renderAfterDocumentEvent.
		document.dispatchEvent(new Event('render-event'))
	}
});