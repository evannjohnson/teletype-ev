### `{{ name }}`

 - **`{{ prototype }}`**
{% if aliases is defined %}
{% for alias in aliases %}
 - _alias_: **`{{ alias }}`**
{% endfor %}
{% endif %}

{% if description is defined %}
{{ description }}
{% else %}
{% if short is defined %}
{{ short }}
{% endif %}
{% endif %}
