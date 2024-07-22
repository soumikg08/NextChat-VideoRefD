POPE_TEST_COMMON_CFG = dict(
    type='POPEVQADataset',
    image_folder='/lustre/fs1/home/sghosh2/NExT-Chat/coco/val2014',
)

DEFAULT_TEST_POPE_VARIANT = dict(
    COCO_POPE_RANDOM_q_a=dict(
        **POPE_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/POPE/coco_pope_random.json',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA.json'
    ),
    COCO_POPE_RANDOM_q_bca=dict(
        **POPE_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/POPE/coco_pope_random.json',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA_BCoT.json'
    ),
    COCO_POPE_POPULAR_q_a=dict(
        **POPE_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/POPE/coco_pope_popular.json',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA.json'
    ),
    COCO_POPE_POPULAR_q_bca=dict(
        **POPE_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/POPE/coco_pope_popular.json',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA_BCoT.json'
    ),
    COCO_POPE_ADVERSARIAL_q_a=dict(
        **POPE_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/POPE/coco_pope_adversarial.json',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA.json'
    ),
    COCO_POPE_ADVERSARIAL_q_bca=dict(
        **POPE_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/POPE/coco_pope_adversarial.json',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA_BCoT.json'
    ),
)

# names = ['COCO_POPE_RANDOM', 'COCO_POPE_POPULAR', 'COCO_POPE_ADVERSARIAL']
# versions = ['q_a', 'q_bca']
# templates = ['VQA', 'VQA_BCoT']
#
# for n in names:
#     for v, t in zip(versions, templates):
#         print(f"""{n}_{v}=dict(
#     **POPE_TEST_COMMON_CFG,
#     filename=f'{{fileDirname}}/../../../data/{n.lower()}.jsonl',
#     template_file=r'{{{fileDirname}}}/template/{t}.json'
# ),"""
#               )
