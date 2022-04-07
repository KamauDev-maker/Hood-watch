export class Quote {
    showInfo: boolean;
    constructor(public id:number,public name:string,public quotes:string,public author:string,public likes:number,public dislikes:number){
        this.showInfo=false
    }

}
