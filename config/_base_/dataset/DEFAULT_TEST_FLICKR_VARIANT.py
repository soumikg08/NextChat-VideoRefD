FLICKR_TEST_COMMON_CFG = dict(
    type='FlickrDataset',
    image_folder=r'/data/public/multimodal/multimodal_data/flickr30k/flickr30k-images',
    max_dynamic_size=None,
)

DEFAULT_TEST_FLICKR_VARIANT = dict(
    FLICKR_EVAL_with_box=dict(
        **FLICKR_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/CWB_flickr30k_eval.jsonl',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/flickr30k.json',
    ),
    FLICKR_EVAL_without_box=dict(
        **FLICKR_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/CWB_flickr30k_eval.jsonl',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/image_cap.json',
    ),
    FLICKR_TEST_with_box=dict(
        **FLICKR_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/CWB_flickr30k_test.jsonl',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/template/flickr30k.json',
    ),
    FLICKR_TEST_without_box=dict(
        **FLICKR_TEST_COMMON_CFG,
        filename='/lustre/fs1/home/sghosh2/NExT-Chat/additional/CWB_flickr30k_test.jsonl',
        template_file='/lustre/fs1/home/sghosh2/NExT-Chat/config/_base_/dataset/templatee/image_cap.json',
    ),
)
