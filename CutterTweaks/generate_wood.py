import json

OUTPUT_DIR = './data/minecraft/recipes/'

WOOD_TYPES = ('oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove')
STEM_TYPES = ('crimson', 'warped')

def write_file(from_wood, to_wood, count):
	new_json = {
		"type": "minecraft:stonecutting",
		"ingredient": {
			"item": f"minecraft:{from_wood}"
		},
		"result": f"minecraft:{to_wood}",
		"count": count
	}
	
	with open(OUTPUT_DIR + f"{to_wood}_from_{from_wood}_stonecutting.json", 'w') as file:
		json.dump(new_json, file, indent=4)

### PLANKS
def planks_to_stairs():
	for wood in WOOD_TYPES + STEM_TYPES:
		write_file(f"{wood}_planks", f"{wood}_stairs", 1)

def planks_to_slabs():
	for wood in WOOD_TYPES + STEM_TYPES:
		write_file(f"{wood}_planks", f"{wood}_slab", 2)

def planks_to_fence():
	for wood in WOOD_TYPES + STEM_TYPES:
		write_file(f"{wood}_planks", f"{wood}_fence", 1)

def planks_to_fence_gate():
	for wood in WOOD_TYPES + STEM_TYPES:
		write_file(f"{wood}_planks", f"{wood}_fence_gate", 1)


### WOOD
def wood_to_planks():
	for wood in WOOD_TYPES:
		write_file(f"{wood}_wood", f"{wood}_planks", 4)
			
	for stem in STEM_TYPES:
		write_file(f"{stem}_hyphae", f"{stem}_planks", 4)
		
def wood_to_stripped_wood():
	for wood in WOOD_TYPES:
		write_file(f"{wood}_wood", f"stripped_{wood}_wood", 1)
			
	for stem in STEM_TYPES:
		write_file(f"{stem}_hyphae", f"stripped_{stem}_hyphae", 1)

def wood_to_log():
	for wood in WOOD_TYPES:
		write_file(f"{wood}_wood", f"{wood}_log", 1)
			
	for stem in STEM_TYPES:
		write_file(f"{stem}_hyphae", f"{stem}_stem", 1)
	
### LOGS
def log_to_planks():
	for wood in WOOD_TYPES:
		write_file(f"{wood}_log", f"{wood}_planks", 4)
			
	for stem in STEM_TYPES:
		write_file(f"{stem}_stem", f"{stem}_planks", 4)
	
def log_to_stripped_log():
	for wood in WOOD_TYPES:
		write_file(f"{wood}_log", f"stripped_{wood}_log", 1)
			
	for stem in STEM_TYPES:
		write_file(f"{stem}_stem", f"stripped_{stem}_stem", 1)
	
def log_to_wood():
	for wood in WOOD_TYPES:
		write_file(f"{wood}_log", f"{wood}_wood", 1)
			
	for stem in STEM_TYPES:
		write_file(f"{stem}_stem", f"{stem}_hyphae", 1)


### STRIPPED
def stripped_wood_to_planks():
	for wood in WOOD_TYPES:
		write_file(f"stripped_{wood}_wood", f"{wood}_planks", 4)
			
	for stem in STEM_TYPES:
		write_file(f"stripped_{stem}_hyphae", f"{stem}_planks", 4)
	
def stripped_wood_to_stripped_log():
	for wood in WOOD_TYPES:
		write_file(f"stripped_{wood}_wood", f"stripped_{wood}_log", 1)
			
	for stem in STEM_TYPES:
		write_file(f"stripped_{stem}_hyphae", f"stripped_{stem}_stem", 1)
		
def stripped_log_to_planks():
	for wood in WOOD_TYPES:
		write_file(f"stripped_{wood}_log", f"{wood}_planks", 4)
			
	for stem in STEM_TYPES:
		write_file(f"stripped_{stem}_stem", f"{stem}_planks", 4)
	
def stripped_log_to_stripped_wood():
	for wood in WOOD_TYPES:
		write_file(f"stripped_{wood}_log", f"stripped_{wood}_wood", 1)
			
	for stem in STEM_TYPES:
		write_file(f"stripped_{stem}_stem", f"stripped_{stem}_hyphae", 1)


### MAIN
planks_to_stairs()
planks_to_slabs()
planks_to_fence()
planks_to_fence_gate()

wood_to_planks()
wood_to_stripped_wood()
wood_to_log()

log_to_planks()
log_to_stripped_log()
log_to_wood()

stripped_wood_to_planks()
stripped_wood_to_stripped_log()
stripped_log_to_planks()
stripped_log_to_stripped_wood()