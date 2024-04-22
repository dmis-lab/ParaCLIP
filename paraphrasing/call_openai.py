import json
import sys
import time
import openai
import os
import random

from tqdm import tqdm


def get_prompt(given_text, mode, seqlen=50):
    if mode == "cap_to_para":
        prompt = (
            'Paraphrase the given caption "{}" concisely '
            'while preserving the meaning.'
        ).format(given_text)
        
    elif mode == "para_to_para":
        prompt = (
            'Paraphrase the given text "{}" concisely '
            'while preserving the meaning and avoiding use of existing words.'
        ).format(given_text)
        
    else:
        print("There seems to be an error with the \"mode\" argument in the \"get_prompt\" funciton.")
        sys.exit()
        
    return prompt


def request(query):
    completion = None
    for i in range(10):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0301",
                max_tokens=512,
                temperature=1.0,
                top_p=0.1,
                messages=[{"role": "user", "content": query}]
            )
            break
        except openai.error.OpenAIError as e:
            print("Some error happened here.")
            delay_secs = 10.0
            randomness_collision_avoidance = random.randint(0, 1000) / 1000.0
            sleep_dur = delay_secs + randomness_collision_avoidance
            print(f"Error: {e}. Retrying in {round(sleep_dur, 2)} seconds.")
            time.sleep(sleep_dur)
            continue

    if completion is not None:
        return completion["choices"][0]["message"]["content"], completion["usage"]["total_tokens"]
    else:
        return completion, 0


def load_data(caption_path, img_id_path=None, is_caption=True):
    with open(caption_path) as f:
        captions = f.readlines()
        
    res, ids = [],[]
    with open(img_id_path) as g:
        img_ids = g.readlines()
    
    assert len(captions) == len(img_ids)

    # Filter out captions that are too short or long
    filtered = 0
    for caption, img_id in zip(captions, img_ids):
        if (len(caption.split()) > 1) and (len(caption.split()) <= 15):
            res.append(caption.rstrip("\n"))
            ids.append(img_id.rstrip("\n"))
        else:
            filtered += 1

    assert len(res) == len(ids)
    
    return res, ids, filtered


def main():
    # Load data
    captions, img_ids, filtered = load_data(caption_path="sample_data/captions.txt", img_id_path="sample_data/img_ids.txt")
    
    print("Num of target captions: {} (total: {}, filtered: {})".format(str(len(captions)), str(len(captions)+filtered), str(filtered)))

    # Generate paraphrases
    data = []
    progress_bar = tqdm(range(len(captions)))
    
    for idx, (caption, img_id) in enumerate(zip(captions, img_ids)):
        # Call GPT-3.5 API
        paraphrase_1, _ = request(query = get_prompt(caption, mode="cap_to_para"))
        paraphrase_2, _ = request(query = get_prompt(paraphrase_1, mode="para_to_para"))

        ex = {
            "index": idx,
            "image_id": img_id,
            "caption": caption,
            "paraphrase_1": paraphrase_1,
            "paraphrase_2": paraphrase_2,
        }
        
        data.append(ex)
        
        progress_bar.update(1)
        
    # Save outputs
    out_path = "outputs"
    
    os.makedirs(out_path, exist_ok=True)
        
    with open(os.path.join(out_path, "paraphrases.jsonl"), "w") as f:
        for d in data:
            f.write(json.dumps(d) + '\n')


if __name__ == "__main__":
    openai.api_key = "openai API key" # Set your API Key
    
    main()

