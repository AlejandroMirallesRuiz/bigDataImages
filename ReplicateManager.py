import replicate

class ReplicateManager:

    def askImage(image):
        prompt = "Describe me the image. Just use words, not sentences. Follow the next format: Answer: word1, word2, word3, word4, etc."
        pathImages = "./fotos/uploaded/"
        image.writeFile()

        print("Running.......")
        output = replicate.run(
            "yorickvp/llava-13b:e272157381e2a3bf12df3a8edd1f38d1dbd736bbb7437277c8b34175f8fce358",
            input={"image": open( pathImages + image.getName() + ".jpg", "rb"), 
                "prompt": prompt,
                    "max_tokens": 300
                }
        )
        print(pathImages + image.getName())

        print("Results:")

        result = ""
        for item in output:
            result += item.strip().lower()

        return result
    
    def askImageSomething():
        prompt = "Describe me the image. Just use words, not sentences. Follow the next format: Answer: word1, word2, word3, word4, etc."
        
        print("Running.......")
        output = replicate.run(
            "yorickvp/llava-13b:e272157381e2a3bf12df3a8edd1f38d1dbd736bbb7437277c8b34175f8fce358",
            input={"image": open(  "./fotos/uploaded/Bola", "rb"), 
                "prompt": prompt,
                    "max_tokens": 300
                }
        )

        print("Results:")

        result = ""
        for item in output:
            print(item)
            result += item

        return result

# https://replicate.com/yorickvp/llava-13b/api?tab=python

if __name__ == "__main__":
    print(ReplicateManager.askImageSomething())