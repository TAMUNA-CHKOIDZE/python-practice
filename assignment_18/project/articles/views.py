from rest_framework import viewsets, status
from rest_framework.response import Response

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(article_deleted=False)
    serializer_class = ArticleSerializer

    def get_serializer(self, *args, **kwargs):
        fields_param = self.request.query_params.get('fields')

        # ვამოწმებთ, თუ action არის detail (retrieve) view-ზე
        is_detail = self.action == 'retrieve'

        if is_detail:
            # დეტალურზე თუ fields პარამეტრი არსებობს, გავანვითაროთ მასთან ერთად,
            # თუ არადა, გავუშვათ სრული serializer (exclude-ის მიხედვით)
            if fields_param:
                fields = tuple(fields_param.split(','))
                kwargs['fields'] = fields
        else:
            # ლისტინგზე content ველი არ მინდა რომ იყოს, ამიტომ ვქმნი fields-ს,
            # ყველა იმ ველით რომელიც არის serializer-ში, content-ის გარდა
            # თუ fields პარამეტრია JSON-ში ამოვიღებ მხოლოდ title, author-ს)
            allowed_fields = set(self.serializer_class().fields)  # ყველა ველი
            allowed_fields.discard('content')  # content-ის ამოღება
            kwargs['fields'] = tuple(allowed_fields)

        return super().get_serializer(*args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.article_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
