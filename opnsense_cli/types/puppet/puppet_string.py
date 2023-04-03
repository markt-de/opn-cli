from opnsense_cli.types.puppet.base import PuppetCodeFragment


class PuppetString(PuppetCodeFragment):
    TEMPLATE_PROVIDER_translate_json_object_to_puppet_resource = '''
    ${name}: json_object['${name}'],
    '''

    TEMPLATE_PROVIDER_translate_puppet_resource_to_command_args = '''
    args.push('--${name}', puppet_resource[:${name}])
    '''

    TEMPLATE_PROVIDER_translate_puppet_resource_to_command_args_namevar = '''
    args.push('--${name}', puppet_resource[:${name}]) if mode == 'update'
    '''

    TEMPLATE_TYPE_example = '''
    ${name} => 'TODO',
    '''

    TEMPLATE_TYPE_attributes = '''
    ${name}: {
          type: 'String',
          desc: '${help}',
        },
    '''

    TEMPLATE_TYPE_attributes_namevar = '''
    ${name}: {
          type: 'String',
          desc: '${help}',
          behaviour: :namevar,
        },
    '''

    TEMPLATE_TYPE_UNIT_TEST_new_resource = '''
    ${name}: 'TODO',
    '''

    TEMPLATE_TYPE_UNIT_TEST_accepts_parameter = '''
    it 'accepts ${name}' do
          ${click_group}_${click_command}[:${name}] = 'a todo string'
          expect(${click_group}_${click_command}[:${name}]).to eq('a todo string')
        end
    '''

    TEMPLATE_PROVIDER_UNIT_TEST_json = '''
    "${name}": 'TODO',
    '''

    TEMPLATE_PROVIDER_UNIT_TEST_json_namevar = '''
    "${name}": 'example ${click_group}_${click_command} TODO_NUMBER',
    '''

    TEMPLATE_PROVIDER_UNIT_TEST_ruby_hash = '''
    ${name}: 'TODO',
    '''

    TEMPLATE_PROVIDER_UNIT_TEST_ruby_hash_namevar = '''
    ${name}: 'example ${click_group}_${click_command} TODO_NUMBER',
    '''

    TEMPLATE_ACCEPTANCE_TEST_create_item = '''
    ${name} => 'TODO',
    '''

    TEMPLATE_ACCEPTANCE_TEST_create_item_namevar = ''

    TEMPLATE_ACCEPTANCE_TEST_match_item = '''
    expect(r.stdout).to match %r{${name}: TODO}
    '''

    TEMPLATE_ACCEPTANCE_TEST_match_item_namevar = '''
    expect(r.stdout).to match %r{${name}: acceptance test item}
    '''