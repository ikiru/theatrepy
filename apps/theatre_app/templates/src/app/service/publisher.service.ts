import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class PublisherService {
  constructor(private _http: Http) {}

  createPublisher(publisher) {
    return this._http
      .post("/publisher", publisher)
      .map(data => data.json())
      .toPromise();
  }
  getPublisher(publisher) {
    return this._http
      .get("/publisher", publisher)
      .map(data => data.json())
      .toPromise();
  }
  updatePublisher(publisher) {
    return this._http
      .patch(`/publisher/${publisher._id}`, publisher)
      .map(data => data.json())
      .toPromise();
  }

  destroyPublisher(id: string) {
    return this._http
      .delete(`/publisher/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
