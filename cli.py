from app import Bootstrap

app = Bootstrap(__name__).instance()

@app.cli.command()
def initdb():
    print('init db - sample cli')

@app.cli.command()
def routes():
    'Display registered routes'
    rules = []
    for rule in self.app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)