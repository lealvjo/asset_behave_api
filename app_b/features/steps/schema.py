from behave import then

@then(u'deve ser retornado de acordo com o schema "{schema_file}"')
def step_impl(context, schema_file):
    context.support.validate_schema(schema_file, context.body.json())