
AREAS = [
    # {
    #     'id': 0,
    #     'name': 'republica mobiliado',
    #     'requests': [
    #         'https://www.quintoandar.com.br/api/search?q=(and%20area:[28,600](and%20custo:[500,4000](and%20(and%20amenidades:%27AR_CONDICIONADO%27amenidades:%27Mobiliado%27)(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D))))&fq=local:[%27-23.515803954316077,-46.73652267460113%27,%27-23.602662769254326,-46.548931113484855%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.559233361785203%2C-46.642726894042994%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(start)
    #         for start in [11 * idx for idx in range(10000)]
    #     ]
    # },
    # {
    #     'id': 1,
    #     'name': 'all',
    #     'requests': [
    #         'https://www.quintoandar.com.br/api/search?q=matchall&fq=local:[%27-23.51494084726495,-46.76240062717682%27,%27-23.598176996016864,-46.552922240499015%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.556558921640907%2C-46.657661433837916%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(start)
    #         for start in [11*idx for idx in range(10000)]
    #     ]
    # },
    {
        'id': 2,
        'name': 'oscar freire mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.55384775333919,-46.67887495744742%27,%27-23.566956776290077,-46.66578255828006%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.560402264814634%2C-46.67232875786374%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 3,
        'name': 'oscar freire nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.55384775333919,-46.678703296070466%27,%27-23.566956776290077,-46.665610896903104%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.560402264814634%2C-46.672157096486785%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 4,
        'name': 'fradique coutinho mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.564481492972686,-46.68590170026965%27,%27-23.567758606087352,-46.68262860047781%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.56612004953002%2C-46.68426515037373%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 5,
        'name': 'fradique coutinho nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.56453066379505,-46.68590170026965%27,%27-23.567807775683015,-46.68262860047781%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.56616921973903%2C-46.68426515037373%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 6,
        'name': 'faria lima mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.565644539609675,-46.69483133624209%27,%27-23.568921623708075,-46.69155823645025%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.567283081658875%2C-46.69319478634617%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 7,
        'name': 'faria lima nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.56564945664921,-46.69484206507815%27,%27-23.568926540624936,-46.69156896528631%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.567287998637074%2C-46.69320551518223%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 8,
        'name': 'pinheiros mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.563165763412123,-46.70619355031113%27,%27-23.569719973530137,-46.699647350727446%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.56644286847113%2C-46.70292045051929%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 9,
        'name': 'pinheiros nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.563264106023396,-46.706247194491425%27,%27-23.569818311234503,-46.699700994907744%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.566541208628948%2C-46.702974094699584%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 10,
        'name': 'butanta mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.570987202333285,-46.70893484937608%27,%27-23.572625687950026,-46.70729829948016%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.571806445141654%2C-46.70811657442812%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 11,
        'name': 'butanta nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.570987202333285,-46.70893484937608%27,%27-23.572625687950026,-46.70729829948016%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.571806445141654%2C-46.70811657442812%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 12,
        'name': 'morumbi mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.58440108914083,-46.72510780119933%27,%27-23.587677705104948,-46.72183470140749%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.58603939712289%2C-46.72347125130341%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 13,
        'name': 'morumbi nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.58440108914083,-46.72511316561736%27,%27-23.587677705104948,-46.72184006582552%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.58603939712289%2C-46.72347661572144%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 14,
        'name': 'paulista mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.551891564529583,-46.66529521116536%27,%27-23.55844633705661,-46.658749011581676%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.555168950793096%2C-46.66202211137352%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 15,
        'name': 'paulista nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.551921069851964,-46.66529521116536%27,%27-23.55847584090746,-46.658749011581676%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.55519845537971%2C-46.66202211137352%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 16,
        'name': 'higienopolis mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.54560113713189,-46.655807842454294%27,%27-23.552156223344134,-46.64926164287061%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.548878680238012%2C-46.65253474266245%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 17,
        'name': 'higienopolis nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.54565430973154,-46.65568982525764%27,%27-23.55220939329255,-46.64914362567396%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.548931851512044%2C-46.6524167254658%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 18,
        'name': 'republica mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3700](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)(and%20tipo:%27Apartamento%27amenidades:%27Mobiliado%27)))&fq=local:[%27-23.540756102056566,-46.645787109574655%27,%27-23.54731142982269,-46.639240909990974%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.54403376593963%2C-46.642514009782815%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
    {
        'id': 19,
        'name': 'republica nao mobiliado',
        'requests': [
            'https://www.quintoandar.com.br/api/search?q=(and%20custo:[500,3000](and%20(or%20quartos:%271%27%20quartos:%272%27%20quartos:%273%27%20quartos:[4,%7D)tipo:%27Apartamento%27))&fq=local:[%27-23.54065774260415,-46.645765651902536%27,%27-23.547213075273596,-46.639219452318855%27]&return=id,foto_capa,aluguel,area,quartos,custo,photos,photo_titles,variant_images,variant_images_titles,endereco,regiao_nome,cidade,visit_status,special_conditions,listing_tags,tipo,promotions&size=11&q.parser=structured&expr.distance=floor(haversin(-23.54393540893887%2C-46.642492552110696%2Clocal.latitude%2Clocal.longitude)*1000*0.002)&expr.rank=((-10*distance%2Brelevance_score)*(0.1))&sort=rank%20desc&start={}'.format(
                start)
            for start in [11 * idx for idx in range(10000)]
        ]
    },
]
