GQA_TEST_COMMON_CFG = dict(
    type='GQADataset',
    image_folder='/datasets/GQA/images',
    scene_graph_file=None,
    scene_graph_index=None,
)

# use standard q-a mode
DEFAULT_TEST_GQA_VARIANT = dict(
    GQA_Q_A_BALANCED=dict(
        **GQA_TEST_COMMON_CFG, version="q-a", template_file="/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA.json",
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/gqa_testdev_balanced_questions.jsonl'
    ),
    GQA_Q_C_BALANCED=dict(
        **GQA_TEST_COMMON_CFG, version="q-a", template_file="/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA_CoT.json",
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/gqa_testdev_balanced_questions.jsonl'
    ),
    GQA_Q_BC_BALANCED=dict(
        **GQA_TEST_COMMON_CFG, version="q-a", template_file="/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA_BCoT.json",
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/gqa_testdev_balanced_questions.jsonl'
    ),

    GQA_Q_A=dict(
        **GQA_TEST_COMMON_CFG, version="q-a", template_file="/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA.json",
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/gqa_testdev_all_questions.jsonl',
    ),
    GQA_Q_C=dict(
        **GQA_TEST_COMMON_CFG, version="q-a", template_file="/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA_CoT.json",
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/gqa_testdev_all_questions.jsonl',
    ),
    GQA_Q_BC=dict(
        **GQA_TEST_COMMON_CFG, version="q-a", template_file="/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/VQA_BCoT.json",
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/gqa_testdev_all_questions.jsonl',
    ),
)
