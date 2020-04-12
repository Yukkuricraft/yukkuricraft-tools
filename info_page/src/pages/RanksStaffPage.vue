<template>
	<normal-page parallax-class="parallax-people">
		<template v-slot:parallax>
			<h1>Ranks and Staff</h1>
		</template>

		<h2 id="ranks">Ranks</h2>
		<p>
			Yukkuricraft has many different ranks. Here is a brief description of them, and what sets them apart
			from each other.
		</p>

		<h3 id="public-ranks">Public ranks</h3>
		<p>These are ranks most commonly seen on members of the community.</p>

		<dl class="row">
			<dt class="col-sm-3 col-md-2">Infant:</dt>
			<dd class="col-sm-9 col-md-10">
				Just joined the server, has not completed the quiz. This is a new person who has not yet mentally
				involved themselves with the server or the community.
			</dd>
			<dt class="col-sm-3 col-md-2">Child:</dt>
			<dd class="col-sm-9 col-md-10">
				Someone who's completed the quiz. This is the rank that people will go through during their first
				few days on the server. Children can set up to 3 homes.
			</dd>
			<dt class="col-sm-3 col-md-2">Adult:</dt>
			<dd class="col-sm-9 col-md-10">
				Someone who has at least a total of 4 days (96 hours) worth of activity on the server. This person
				has devoted a lot of their time on the server and is now considered an active member of the
				community. Adults and up are allowed to use items like fire and lava. Adults can set up to 5 homes.
			</dd>
			<dt class="col-sm-3 col-md-2">Senior:</dt>
			<dd class="col-sm-9 col-md-10">
				Someone who has at least a total of <strong>10</strong> days (240 hours) worth of activity. Can set
				up to 10 homes at once.
			</dd>
			<dt class="col-sm-3 col-md-2">Elder:</dt>
			<dd class="col-sm-9 col-md-10">
				This rank represents dedication and big positive involvement with the community and staff. Elders
				are specifically chosen and voted on by the staff. If you are an Elder, that means you're a positive
				force within the community, and have been noticed for your actions. You're one of the community
				leaders. Inactive and troublesome elders can be demoted. This is mostly just a pretty title! Elders
				can set up to 15 homes.
			</dd>
		</dl>

		<h3 id="staff-ranks">Staff ranks</h3>
		<p>
			The following list consists of the main permission-tampering ranks that are most regularly seen. These
			ranks are also allowed to hack their games so as long as they do not use the hacks for cheating in
			survival mode.
		</p>

		<p>
			There are also special "Titles" within the staff ranks. "Titles" are just that. Titles. They're a way to
			differentiate slightly different purposes within the same overall rank.
		</p>

		<dl class="row">
			<dt class="col-sm-3 col-md-2">Mediator:</dt>
			<dd class="col-sm-9 col-md-10">
				Someone who has been assigned the privilege of moderating the server community. Their duty is to
				look after everyone and make sure they're on their best behavior. They are capable of building in
				Gensokyo but are not assigned to.

				<br/>
				<br/>
				<dl class="row">
					<dt class="col-sm-3 col-md-2"><i>The [Advisor] Title</i>:</dt>
					<dd class="col-sm-9 col-md-10">
						A mediator with extensive historical knowledge of the Yukkuricraft community. While equal to
						other mediators, these members are respected within the staff body for having been around
						since YC's early days (~2011) as a community.
					</dd>
				</dl>
			</dd>
			<dt class="col-sm-3 col-md-2">Youkai Builder:</dt>
			<dd class="col-sm-9 col-md-10">
				Someone who has been assigned the privilege of building in Gensokyo, allowing them to modify and
				change what they deem necessary. These peeps have some real building talent, and are responsible for
				many of Gensokyo's structures.

				<br/>
				<br/>
				<dl class="row">
					<dt class="col-sm-3 col-md-2"><i>The [Lead] Title</i>:</dt>
					<dd class="col-sm-9 col-md-10">
						Builders with this title are designated as the "heads" of the bunch. These builders are
						generally willing to go the extra mile to organize and head large-scale projects for
						Gensokyo.
					</dd>
				</dl>
			</dd>
			<dt class="col-sm-3 col-md-2">Sysadmin:</dt>
			<dd class="col-sm-9 col-md-10">
				These staff are responsible for the technology side of Yukkuricraft. Think server, plugins, discord
				bots, etc. While sysadmin have access to all commands and are effectively similar to admins, they do
				not outrank Yukkuri Admins in regards to the community.
			</dd>
			<dt class="col-sm-3 col-md-2">Yukkuri Admin:</dt>
			<dd class="col-sm-9 col-md-10">
				Yukkuri Admins are the highest roles on the server, they have access to every command and have the
				final say in decisions. These admins are entrusted to handle or oversee almost any major issue
				within the community overall and see it resolved amicably.

				<br/>
				<br/>
				<dl class="row">
					<dt class="col-sm-3 col-md-2"><i> The [Owner] Title</i>:</dt>
					<dd class="col-sm-9 col-md-10">
						These people have access to the serverbox and have completely control over the
						server's existence.
					</dd>
				</dl>
			</dd>
		</dl>

		<h3>Special ranks</h3>
		<p>
			The following ranks are special ranks that you don't see as often, but serve a purpose for specific
			circumstances.
		</p>

		<dl class="row">
			<dt class="col-sm-3 col-md-2">Probation:</dt>
			<dd class="col-sm-9 col-md-10">
				People who have been previously permanently banned, but are being given another chance to redeem
				their self. If this person screws up even once, they will most likely go back to being permanently
				banned and will no longer receive any chances for redemption in the future. It takes a lot to get
				this rank, you'd have to basically try to get it in order to get it.
			</dd>
			<dt class="col-sm-3 col-md-2">Temp. Youkai:</dt>
			<dd class="col-sm-9 col-md-10">
				Someone who has been temporarily granted permission to build in Gensokyo in order to give focus to
				specific projects without actually being a full-fledged builder.
			</dd>
			<dt class="col-sm-3 col-md-2">Retired:</dt>
			<dd class="col-sm-9 col-md-10">Someone who used to be on the staff team but is no longer.</dd>
			<dt class="col-sm-3 col-md-2">Legendary:</dt>
			<dd class="col-sm-9 col-md-10">
				Someone who has had a large and positive impact on the server and/or the community, but no longer
				regularly participates, sometimes having left entirely.
			</dd>
		</dl>

		<h2 id="staff">Our Staff</h2>
		<table class="table smaller-sm-text" v-for="staffGroup in staff">
			<colgroup>
				<col style="width: 20%;">
				<template v-if="staffGroup.hasDescription">
					<col style="width: 30%;">
					<col style="width: 50%;">
				</template>
				<col v-else style="width: 80%;">
			</colgroup>
			<thead>
			<tr>
				<th colspan="1">{{ staffGroup.displayName }}</th>
				<th :colspan="staffGroup.hasDescription ? 2 : 1">MC Accounts</th>
			</tr>
			</thead>
			<tr v-for="staff in staffGroup.members">
				<td>{{ staff.name }}</td>
				<td>
					<ul v-if="staff.mcAccounts.length > 1" class="list-unstyled">
						<li v-for="mcAccount in staff.mcAccounts">
							<img :src="'https://mc-heads.net/avatar/' + mcAccount.uuid + '/32'" :alt="mcAccount.name">
							{{ mcAccount.name }}
						</li>
					</ul>
					<div v-else>
						<img :src="'https://mc-heads.net/avatar/' + staff.mcAccounts[0].uuid + '/32'"
							 :alt="staff.mcAccounts[0].name">
						{{ staff.mcAccounts[0].name }}
					</div>
				</td>
				<td v-if="staffGroup.hasDescription">{{ staff.description }}</td>
			</tr>
		</table>

		<p>
			<strong><span style="font-size: xx-large; color: #ff0000;">DISCLAIMER:</span></strong> Mediators <em>do
			not</em> have authority over builders, they are completely even ranks that do not overpower each other
			unless it's in the category their rank is designed for. If the subject is about building decisions and
			choices, builders have first say. If it's about banning/kicking/rollback/lookups, mediators have first
			say.
		</p>
	</normal-page>
</template>

<script>
	import InfoFooter from "../components/InfoFooter";
	import ParallaxImage from "../components/ParallaxImage";

	import {staff} from "./staff";
	import NormalPage from "../layout/NormalPage";

	export default {
		components: {
			NormalPage,
			InfoFooter,
			ParallaxImage
		},
		data() {
			return {
				staff: staff
			}
		},
		created() {
			for(let staffGroup of this.staff) {
				for(let staffMember of staffGroup.members) {
					for(let mcAccount of staffMember.mcAccounts) {
						this.mcUsername(mcAccount.uuid, mcAccount.name).then(res => {
							mcAccount.name = res;
						})
					}
				}
			}
		},
		methods: {
			async mcUsername(uuid, fallback) {
				let errorMsg = `Failed to get name for uuid ${uuid}, using fallback ${fallback} instead`;

				try {
					let res = await fetch('https://api.minetools.eu/profile/' + uuid.replaceAll('-', ''));

					if (res.status !== 200) {
						console.warn(errorMsg);
						return fallback;
					} else {
						let profile = await res.json();

						if(typeof profile.error !== 'undefined') {
							console.warn(errorMsg + '. Error: ' + profile.error);
							return fallback;
						}
						else {
							return profile.decoded.profileName
						}
					}
				} catch (e) {
					console.warn(errorMsg + '. Error: ' + e);
					return fallback
				}
			}
		}
	}
</script>