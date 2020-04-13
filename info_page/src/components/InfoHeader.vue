<template>
	<nav id="top-navbar" class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
		<div v-if="inContainer" class="container">
			<slot name="top"></slot>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
					aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<navbar-links id="navbarSupportedContent"></navbar-links>

			<navbar-locale-changer></navbar-locale-changer>
			<slot name="bottom"></slot>
		</div>

		<template v-else>
			<slot name="top"></slot>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
					aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<navbar-links id="navbarSupportedContent"></navbar-links>

			<navbar-locale-changer></navbar-locale-changer>
			<slot name="bottom"></slot>
		</template>
	</nav>
</template>

<script>
	import NavbarLinks from "./NavbarLinks"
	import NavbarLocaleChanger from "./NavbarLocaleChanger"

	export default {
		components: {
			NavbarLinks,
			NavbarLocaleChanger
		},
		props: {
			inContainer: {
				type: Boolean,
				default: true
			}
		}
	}
</script>
