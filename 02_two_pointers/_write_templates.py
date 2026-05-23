import textwrap

CONTENT = textwrap.dedent("""
    # placeholder
""")

target = r"c:\Personal\Ajay_Work_Docs\Grad_Project\DSA\02_two_pointers\templates.py"
with open(target, "w", encoding="utf-8") as f:
    f.write(CONTENT)
print("Written", len(CONTENT), "chars")
