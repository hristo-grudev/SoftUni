from collections import defaultdict

junk = defaultdict(int)
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}

legendary_item = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}

target = False

while not target:
	res = input().split()
	for nii in range(0, len(res), 2):
		key = res[nii + 1].lower()
		if key in legendary_item.keys():
			key_materials[key] += int(res[nii])
			if key_materials[key] >= 250:
				print(f'{legendary_item[key]} obtained!')
				key_materials[key] -= 250
				target = True
				break
		else:
			junk[key] += int(res[nii])
ordered_key_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
for item, qty in ordered_key_materials:
	print(f'{item}: {qty}')

junk = sorted(junk.items(), key=lambda x: (x[0]))
for item, qty in junk:
	print(f'{item}: {qty}')
