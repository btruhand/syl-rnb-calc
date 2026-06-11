const BJIR_CHANGELOG = [
	new ChangelogLine(
		1,
		0,
		0,
		"Adds 'Export All' feature for opposing team; speed stat included in all exports",
	),
	new ChangelogLine(
		1,
		0,
		0,
		"Importing Pokémon with a mega evolution in player's roster auto-updates player's mega Pokémon to match the imported base Pokémon's level, nature, and IVs",
	),
	new ChangelogLine(
		1,
		0,
		0,
		"Toggleable OHKO color coding and speed borders for opposing team based on currently chosen player's Pokémon",
	),
	new ChangelogLine(
		1,
		0,
		0,
		"Opposing team roster now shows base form of mega Pokémon",
	),
	new ChangelogLine(
		1,
		1,
		0,
		"Add 'Sort by name' option for player box; lexicographic ordering, earlier name first",
	),
	new ChangelogLine(
		1,
		1,
		1,
		"Keep Pokémon in their respective boxes when reloading",
	),
	new ChangelogLine(
		1,
		2,
		0,
		"Add 'Sort by speed' option for player box; descendingly sorts by speed stat then lexicographically by name if speeds are equal, earlier name first)",
	),
	new ChangelogLine(
		1,
		2,
		1,
		"Fix hide/show for color coding to work again, it was always shown before",
	),
	new ChangelogLine(
		1,
		2,
		2,
		"Properly sets last trainer on dropdown selection",
	),
	new ChangelogLine(
		1,
		3,
		0,
		"Add color coding and speed border for opposing team's selected Pokémon sprite; rename 'Opponent Color' option to 'Opponent Color/Speed Border'",
	),
	new ChangelogLine(
		1,
		3,
		1,
		"Fix 'Export all' not working with Space tag battle",
	),
	new ChangelogLine(
		1,
		4,
		0,
		"Add 'Auto-detect doubles' option in Field table",
	),
	new ChangelogLine(
		1,
		4,
		1,
		"Fix opposing trainer dropdown incorrectly showing Winstrate Victoria after reload in an edge case",
	),
	new ChangelogLine(
		1,
		5,
		0,
		"Add auto-detect doubles optional feature; Add optional team slots support for double battles",
	),
	new ChangelogLine(1,6,0,"Add 'Auto-detect pseudo/true doubles' optional function"),
	new ChangelogLine(1, 6, 1,"Fix crit state for moves incorrectly obtained from player's Pokémon instead of opposing side when calculating opposing OHKO color"),
	new ChangelogLine(1,6,2,"Fix Fisherman Darian and Phil separated as different fights. Also combine them as one result in the search bar")
];
