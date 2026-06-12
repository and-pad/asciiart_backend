import subprocess


class asciijpg:
    def convert(self, image_path, width=None, height=None, colors=False):
        command = ["jp2a", "--html", "--chars= .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$%█"]

        if colors:
            command.append("--colors")

        if width:
            command.extend([f"--width={str(width)}"])

        if height:
            command.extend([f"--height={str(height)}"])

        command.append(image_path)
        
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        #print(result.stdout)
        
        return result.stdout
