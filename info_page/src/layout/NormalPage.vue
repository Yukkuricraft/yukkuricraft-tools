<template>
	<div>
		<info-header></info-header>
		<parallax-image :class="parallaxClass">
			<slot name="parallax"></slot>
		</parallax-image>

		<div class="container">
			<slot></slot>
			<info-footer></info-footer>
		</div>
	</div>
</template>

<script>
	import InfoHeader from "../components/InfoHeader";
	import InfoFooter from "../components/InfoFooter";
	import ParallaxImage from "../components/ParallaxImage";

	export default {
		components: {
			InfoHeader,
			InfoFooter,
			ParallaxImage
		},
		props: {
			parallaxClass: String
		}
	}
</script>