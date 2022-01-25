{
    'name': "test",
    'version': '1.0',
    'depends': ['base'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'view/pass.xml',
        'reports/passport_card.xml',
        'reports/report.xml',

    ],
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}