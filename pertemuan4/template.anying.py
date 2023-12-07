class SimpleTemplateEngine:
    def __init__(self, template):
        self.template = template

    def render(self, variables):
        result = self.template

        for key, value in variables.items():
            placeholder = "{N " + key + " N}"
            result = result.replace(placeholder, str(value))

        return result


# Contoh penggunaan template engine
template_str = "Halo, {N nama N}! Selamat datang di {versity}."

# Membuat instance dari template engine
template_engine = SimpleTemplateEngine(template_str)

# Variabel yang akan disubstitusi
data = {'nama': 'John', 'versity': 'Universitas ABC'}

# Render template dengan variabel
result = template_engine.render(data)

# Tampilkan hasilnya
print(result)
