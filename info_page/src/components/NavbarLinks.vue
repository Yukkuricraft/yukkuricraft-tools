<template>
	<div class="collapse navbar-collapse">
		<ul class="navbar-nav mr-auto">
			<router-link :to="{name: 'info'}" v-slot="{ href, navigate, isExactActive }">
				<li class="nav-item" :class="[isExactActive && 'active']">
					<a class="nav-link" :href="href" @click="navigate">Info</a>
				</li>
			</router-link>
			<router-link :to="{name: 'ranks_staff'}" v-slot="{ href, navigate, isExactActive }">
				<li class="nav-item" :class="[isExactActive && 'active']">
					<a class="nav-link" :href="href" @click="navigate">Ranks and Staff</a>
				</li>
			</router-link>
			<router-link :to="{name: 'rules'}" v-slot="{ href, navigate, isExactActive }">
				<li class="nav-item" :class="[isExactActive && 'active']">
					<a class="nav-link" :href="href" @click="navigate">Rules</a>
				</li>
			</router-link>
			<router-link :to="{name: 'commands'}" v-slot="{ href, navigate, isExactActive }">
				<li class="nav-item" :class="[isExactActive && 'active']">
					<a class="nav-link" :href="href" @click="navigate">Commands</a>
				</li>
			</router-link>
			<li class="nav-item"><a class="nav-link" href="https://yukkuricraft.net">Forums</a></li>
		</ul>
	</div>
</template>