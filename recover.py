import json
import os

log_path = r"C:\Users\kalea\.gemini\antigravity-ide\brain\eb108f57-8a9e-4dd4-8c2d-566d9d9c717b\.system_generated\logs\transcript.jsonl"
out_path = r"D:\Plastroots_Website\recovered_ps_data.js"

if not os.path.exists(log_path):
    print("Log not found")
    exit()

best_content = None

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            # look for write_to_file
            if "tool_calls" in data:
                for call in data["tool_calls"]:
                    if call.get("name") == "default_api:write_to_file":
                        args = call.get("arguments", {})
                        if "ProductsServicesData.js" in args.get("TargetFile", ""):
                            best_content = args.get("CodeContent")
                    if call.get("name") == "default_api:replace_file_content":
                        args = call.get("arguments", {})
                        if "ProductsServicesData.js" in args.get("TargetFile", ""):
                            print("Found replace_file_content for ps data")
                            # this doesn't have the full file
        except Exception as e:
            pass

if best_content:
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(best_content)
    print("Recovered from write_to_file!")
else:
    print("No write_to_file found for ProductsServicesData.js")
