<template>
	<normal-page parallax-class="parallax-download">
		<template v-slot:parallax>
			<h1>"Gensokyo ~ The Second Dream" Map download</h1>
			<a class="btn btn-primary" href="https://mega.nz/#F!5hU2HCJC!IpwU8ZjpwSALOgLjoZtNlA">Downloads</a>
		</template>

		<div class="alert alert-warning mt-3" role="alert" style="font-size: 85%">
			<h2 class="alert-heading h5">Missing and broken features in Vanilla</h2>
			<p class="mb-2">
				While we try as best we can to give you a great experience, some things might not work correctly. Our
				recommendation is always to explore the map on the server for the best experience. Some things that
				might
				break include (not an exclusive list):
			</p>
			<ul>
				<li>Grass growing on dirt</li>
				<li>Monsters spawning</li>
				<li>Ice/snow forming and melting</li>
				<li>Portals/teleportation not working</li>
				<li>Vegetation growing</li>
			</ul>
		</div>

		<p v-if="showI18nExample">message: {{ $t('hello') }}</p>

		<p>
			<strong>CHROME USERS</strong> - Mega is known to have issues downloading on Chrome. If you are using Chrome
			and
			having difficulty downloading, please temporarily use Firefox or some other browser of your choice to
			download
			from that link.
		</p>
	</normal-page>
</template>

<i18n>
	{
	"en": {
	"hello": "hello world!"
	},
	"ja": {
	"hello": "こんにちは、世界！"
	}
	}
</i18n>

<script>
	import NormalPage from "../../layout/NormalPage";

	export default {
		components: {NormalPage},
		computed: {
			showI18nExample() {
				return false
			}
		}
	}
</script>