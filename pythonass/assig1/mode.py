import json
people_route = '''
{
	"end_points": [ "A", "B", "C", "D" ],
	"switches": [ "S1", "S2", "S3", "S4" ],
	"links" : [
		{
			"points" : [ "A", "S1" ],
			"capacity" : 10.0
		},
                {
                        "points" : [ "B", "S2" ],
                        "capacity" : 10.0
                },
                {
                        "points" : [ "D", "S4" ],
                        "capacity" : 10.0
                },
                {
                        "points" : [ "S1", "S4" ],
                        "capacity" : 10.0
                },
                {
                        "points" : [ "S1", "S3" ],
                        "capacity" : 10.0
                },
                {
                        "points" : [ "S2", "S3" ],
                        "capacity" : 10.0
                },
                {
                        "points" : [ "S4", "C" ],
                        "capacity" : 10.0
                },
                {
                        "points" : [ "S3", "C" ],
                        "capacity" : 10.0
                }
	],
	"possible_circuits" : [
		["D", "S4", "C"],
		["C", "S4", "D"],
		["A", "S1", "S3", "C"],
		["A", "S1", "S3", "C"],
		["C", "S4", "S1", "A"],
		["C", "S3", "S1", "A"],
		["B", "S2", "S3", "C"],
		["C", "S3", "S2", "B"],
		["B", "S2", "S3", "S1", "A"],
		["A", "S1", "S3", "S2", "B"],
		["D", "S4", "S1", "S3", "S2", "B"],
		["B", "S2", "S3", "S1", "S4", "D"],
		["A", "S1", "S4", "D"],
		["D", "S4", "S1", "A"]
	],
	"simulation" : {
		"duration" : 11,
		"demands" : [
			{
				"start-time" : 1,
				"end-time" : 5,
				"end-points" : ["A", "C"],
				"demand" : 10.0
			},
			{
				"start-time" : 2,
				"end-time" : 10,
				"end-points" : ["B", "C"],
				"demand" : 10.0
			},
                        {
                                "start-time" : 6,
                                "end-time" : 10,
                                "end-points" : ["D", "C"],
                                "demand" : 10.0
                        },
                        {
                                "start-time" : 7,
                                "end-time" : 10,
                                "end-points" : ["A", "C"],
                                "demand" : 10.0
                        }
		]
	}
}
'''
data = json.loads(people_route)
for demands in data['simulation']['demands']:
    print( 'demand reservation: ' ,demands['end-points'] )

    
