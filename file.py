

KNOWLEDGE = ["write", "list", "label", "name", "state", "define", "count", "describe", "draw", "find", "identify", "match",
                        "quote", "recall", "recite", "Sequence", "tell", "arrange", "duplicate", "memorize", "order", "outline",
                        "recognize", "relate", "repeat", "reproduce", "select", "choose", "copy", "how", "listen", "locate",
						"memorise", "observe", "omit", "read", "recognise", "record", "remember", "retell", "spell",
						"trace", "what", "when", "where", "which", "who", "why"]

COMPREHENSION =["Explain", "summarize", "paraphrase", "illustrate", "conclude", "demonstrate", "discuss",
						   "generalize", "identify", "interpret", "predict", "report", "restate", "review", "classify",
						   "convert", "defend", "distinguish", "estimate", "express", "extend", "give example", "indicate",
						   "infer", "locate", "recognize", "rewrite", "select", "translate", "ask", "cite", "compare",
						   "contrast", "generalise", "give examples", "match", "observe", "outline", "purpose", "relate",
						   "rephrase", "show", "summarise"]

APPLICATION = ["use", "compute", "solve", "demonstrate", "apply", "construct", "change", "choose", "dramatize", "interview",
						 "prepare", "produce", "select", "show", "transfer", "discover", "employ", "illustrate",
						 "interpret", "manipulate","modify", "operate", "practice", "predict", "relate schedule", "sketch",
						 "use write", "act", "aminister", "associate", "build", "calculate", "categorise", "classify",
						 "connect", "correlation", "develop", "dramatise", "experiment", "with", "group", "identify",
						 "link", "make use of", "model", "organise", "perform", "plan", "relate", "represent", "simulate",
						 "summarise", "teach", "translate"]

ANALYSIS= ["analyse", "categorize", "compare", "contrast", "separate", "characterize", "classify", "debate", "deduce",
					  "diagram", "differentiate", "discriminate", "distinguish", "examine", "outline", "relate", "research",
					  "appraise", "breakdown", "calculate", "criticize", "derive", "experiment", "identify", "illustrate",
					  "infer", "interpret", "model", "outline", "point out", "question", "select", "subdivide", "test",
					  "arrange", "assumption", "categorise", "cause and", "effect", "choose", "difference", "discover",
					  "dissect", "distinction", "divide", "establish", "find", "focus", "function", "group", "highlight",
					  "in-depth", "discussion", "inference", "inspect", "investigate", "isolate", "list", "motive", "omit",
					  "order", "organise", "point out", "prioritize", "rank", "reason", "relationships", "reorganise", "see",
					  "similar to", "simplify", "survey", "take part in", "test for", "theme", "comparing"]


EVALUATION = ['appraise', 'argue', 'defend', 'judge', 'select', 'support', 'value', 'critique', 'weigh', 'adapt',"debate", "deduct", "determine", "disprove", "dispute", "effective", "give reason" ]
CREATE=["create", "design", "hypothesize", "invent", "develop", "compose", "construct", "integrate", "make",
					   "organize", "Perform", "plan", "produce", "propose", "rewrite", "arrange", "assemble", "categorize",
					   "collect", "combine", "comply", "devise", "explain", "formulate", "generate", "prepare", "rearrange",
					   "reconstruct", "relate", "reorganize", "revise", "set up", "summarize", "synthesize", "tell", "write",
					   "adapt", "add to", "build", "change", "choose", "combine", "compile", "convert", "delete", "discover",
					   "discuss", "elaborate", "estimate", "experiment", "extend", "happen", "hypothesise", "imagine",
					   "improve", "innovate", "make up", "maximise", "minimise", "model", "modify", "original", "originate",
					   "predict", "reframe", "simplify", "solve", "speculate", "substitute", "suppose", "tabulate", "test",
					   "theorise", "think", "transform", "visualise"]

string1 = ' Give reason for the following algo' \
          'Explain the following' #look into EVALUATION LIST
knowledge = [ele for ele in KNOWLEDGE if(ele in string1.lower())]
print("does string belongs to knowledge class :", bool(knowledge))

comprehension = [ele for ele in COMPREHENSION if(ele in string1.lower())]
print("does string belongs to evaluation class :", bool(comprehension))

application = [ele for ele in APPLICATION if(ele in string1.lower())]
print("does string belongs to application class ::", bool(application))

analysis = [ele for ele in ANALYSIS if(ele in string1.lower())]
print("does string belongs to analysis class :", bool(analysis))

create = [ele for ele in CREATE if(ele in string1.lower())]
print("does string belongs to create class :", bool(create))

evaluation = [ele for ele in EVALUATION if(ele in string1.lower())]
print("does string belongs to evaluation class :", bool(evaluation))


