def fun1(Dicts):
    if isinstance(Dicts,list):
            return{"ukupno":{"artikl":[item["naziv"] for item in Dicts],"cijena":sum(item["cijena"]*item["kolicina"]for item in Dicts)}}
print(fun1([{"cijena":8,"naziv":"kruh","kolicina":1}])),\
{"cijena":13,"naziv":"Sok","kolicina":2},\
{"cijena":7,"naziv":"Upaljac","kolicina":1}