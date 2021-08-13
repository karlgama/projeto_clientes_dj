from rest_framework import serializers
from clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    # o nome tem que ser validate_campo se não, não vai ser chamado o método
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ser válido")
        return cpf
    def validate_nome(self, nome:str):
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua números nesse campo")
        return nome
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ser válido")
        return rg
    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError("O celular ter no mínimo 11 caracteres")
        return celular